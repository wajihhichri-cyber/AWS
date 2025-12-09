"""Application configuration settings."""
import os
import json
import boto3


class Config:
    """Base configuration."""
    
    # Database
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL', 'sqlite:///cybertek.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    
    # Security
    SECRET_KEY = None  # Will be set dynamically
    
    # Application
    DEBUG = False
    TESTING = False
    HOST = '0.0.0.0'
    PORT = 5000
    
    @staticmethod
    def get_secret_key():
        """Retrieve secret key from AWS Secrets Manager or use default."""
        try:
            client = boto3.client('secretsmanager', region_name='us-west-2')
            response = client.get_secret_value(SecretId='flask/session-key')
            secret_json = json.loads(response['SecretString'])
            return secret_json['flask_session_key']
        except Exception:
            return 'cybertek-secret-key-change-in-production'


class DevelopmentConfig(Config):
    """Development configuration."""
    DEBUG = True


class ProductionConfig(Config):
    """Production configuration."""
    DEBUG = False


class TestingConfig(Config):
    """Testing configuration."""
    TESTING = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///test_cybertek.db'


# Configuration dictionary
config = {
    'development': DevelopmentConfig,
    'production': ProductionConfig,
    'testing': TestingConfig,
    'default': DevelopmentConfig
}
