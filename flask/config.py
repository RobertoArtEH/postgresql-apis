class Config:
  SECRET_KEY = 'SUPER_SECRET'

  # postgresql://username:password@host:port/database
  SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:toor@127.0.0.1:5432/datastorage'