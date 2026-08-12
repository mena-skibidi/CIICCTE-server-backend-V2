from sqlmodel import Field, Session, SQLModel, create_engine, select, Relationship


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

def create_base_roles():
    with Session(engine) as session:
        role1_statement = select(roles).where(roles.id == 1)
        role1_exists_check = session.exec(role1_statement).first()
        if role1_exists_check:
            print("El rol de admin ya existe, skippeando paso")
        else:
            print("El rol de admin no existe, creandolo")
            admin_role = roles(nombre_rol="admin")
            session.add(admin_role)
            session.commit()

        role2_statement = select(roles).where(roles.id == 2)
        role2_exists_check = session.exec(role2_statement).first()
        if role2_exists_check:
            print("El rol de usuario ya existe, skippeando paso")
        else:
            print("El rol de usuario no existe, creandolo")
            usuario_role = roles(nombre_rol="usuario")
            session.add(usuario_role)
            session.commit()

def create_cuenta():
    with Session as session:
