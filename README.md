# SQLAlchemy

SQLAlchemy is a powerful SQL toolkit and Object Relational Mapper (ORM) for Python. It provides a full suite of well-known enterprise-level persistence patterns, designed for efficient and high-performing database access.

## Features

- Full ORM capabilities for mapping classes to database tables
- Database-agnostic SQL expression language
- Support for multiple database backends (PostgreSQL, MySQL, SQLite, Oracle, etc.)
- Connection pooling and transaction management
- Schema generation and migrations (with Alembic)

## Installation

```bash
pip install SQLAlchemy
```

## Run Models

```bash
python lib/models.py
```

## Quick Start

```python
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import declarative_base, sessionmaker

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    name = Column(String)

engine = create_engine('sqlite:///example.db')
Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()

new_user = User(name="Alice")
session.add(new_user)
session.commit()
```

## Documentation

- [Official Documentation](https://docs.sqlalchemy.org/)
- [Getting Started Guide](https://docs.sqlalchemy.org/en/20/intro.html)

## License

SQLAlchemy is released under the MIT License.