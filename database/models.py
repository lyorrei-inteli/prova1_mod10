from sqlalchemy import Boolean, Column, Integer, String, Text
from database.database import db

class Pedido(db.Model):
  __tablename__ = 'pedidos'

  id = Column(Integer, primary_key=True, autoincrement=True)
  user_name = Column(String(50), nullable=False)
  user_email = Column(String(50), nullable=False)
  description = Column(Text(), nullable=False)

  def __repr__(self):
    return f'<Pedido:[id:{self.id}, user_name:{self.user_name}, user_email:{self.user_email}, description:{self.description}]>'
  
  def serialize(self):
    return {
      "id": self.id,
      "user_name": self.user_name,
      "user_email": self.user_email,
      "description": self.description
     }