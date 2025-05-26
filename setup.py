# ===== setup.py =====
from setuptools import setup, find_packages

setup(
    name='AetherLog',
    version='0.1.0',
    description='AetherLog: LLM-KG Synergistic Framework for Log-based Root Cause Analysis',
    author='AetherLog Authors',
    author_email='contact@example.com',
    url='https://github.com/ISSRE25-Submission-56/AetherLog',
    packages=find_packages(),
    install_requires=[
        'tqdm',
        'openai',
        'scikit-learn',
        'torch',
        'transformers',
        'sentence-transformers',
        'networkx',
        'pyyaml'
    ],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.7',
    entry_points={
        'console_scripts': [
            'aetherlog-preprocess=scripts.preprocess:preprocess_logs',
            'aetherlog-buildkg=scripts.build_kg:main',
            'aetherlog-align=scripts.entity_alignment:align_entities',
            'aetherlog-rca=scripts.rca_pipeline:main',
            'aetherlog-eval=scripts.evaluate:main',
            'aetherlog-recall=scripts.recall_entity:main',
            'aetherlog-prompt=scripts.rca_prompt:main'
        ]
    },
    include_package_data=True,
    zip_safe=False
)
