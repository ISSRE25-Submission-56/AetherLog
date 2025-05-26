import openai
import json
import os

class Summarizer:
    def __init__(self, model_name='gpt-4', max_tokens=512, api_key=''):
        
        self.model_name = model_name
        self.max_tokens = max_tokens
        self.api_key = api_key or os.getenv("OPENAI_API_KEY")
        if not self.api_key:
            raise ValueError("API key is required for summarization.")

        openai.api_key = self.api_key

    def generate_summary(self, text, temperature=0.3):
       
        try:
            response = openai.Completion.create(
                model=self.model_name,
                prompt=f"Please summarize the following text:\n{text}",
                max_tokens=self.max_tokens,
                temperature=temperature,
                n=1,
                stop=None,
                top_p=1,
                frequency_penalty=0.0,
                presence_penalty=0.0
            )
            summary = response.choices[0].text.strip()
            return summary
        except openai.error.OpenAIError as e:
            print(f"Error generating summary: {e}")
            return None

    def summarize_logs(self, log_file_path, output_file_path):
        
        summaries = []
        try:
            with open(log_file_path, 'r') as f:
                logs = json.load(f)
                
            for log in logs:
                log_text = log.get("log_text", "")
                if log_text:
                    print(f"Generating summary for log: {log_text[:30]}...")
                    summary = self.generate_summary(log_text)
                    if summary:
                        summaries.append({
                            'log_id': log.get("log_id", ""),
                            'original': log_text,
                            'summary': summary
                        })
            with open(output_file_path, 'w') as f:
                json.dump(summaries, f, indent=4)

            print(f"Summaries saved to {output_file_path}")
        except Exception as e:
            print(f"Error in summarizing logs: {e}")
    
    def summarize_single_log(self, log_text):
       
        return self.generate_summary(log_text)

