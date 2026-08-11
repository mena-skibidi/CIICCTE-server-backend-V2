from sqlmodel import Field, Session, SQLModel, create_engine, select


class roles(SQLModel, table=True):
    id: int = Field(default=None, primary_key=True)
    nombre_rol: str


class usuarios(SQLModel, table=True):
    id: int = Field(default=None, primary_key=True)
    username: str
    nombre_completo: str
    password_encriptada: str


class cuenta(SQLModel, table=True):
    id: int = Field(default=None, primary_key=True)
    usuarios_id: int = Field(default=None, foreign_key="usuarios.id")
    roles_id: int = Field(default=None, foreign_key="roles.id")


engine = create_engine("postgresql://dbuser:labtest321@db:5432/labdb", echo=True)


def create_tables():
    SQLModel.metadata.create_all(engine, checkfirst=True)

def create_admin_role():
    with Session(engine) as session:
        exists_statement = select(roles).where(roles.id == 0)
        exists_check = session.exec(exists_statement).first()
        if exists_check == True:
            print("El rol de admin ya existe, skippeando paso")
        else:
            print("El rol de admin no existe, creandolo")
            admin_role = roles(0, "admin")
            session.add(admin_role, )
            session.commit()