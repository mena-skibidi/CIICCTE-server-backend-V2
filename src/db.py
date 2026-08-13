from sqlmodel import Field, Session, SQLModel, create_engine, select

# Models

class roles(SQLModel, table=True):
    id: int = Field(default=None, primary_key=True)
    nombre_rol: str


class users(SQLModel, table=True):
    id: int = Field(default=None, primary_key=True)
    username: str = Field(unique=True)
    nombre_completo: str
    password_encriptada: str
    roles_id: int = Field(default=None, foreign_key="roles.id")


engine = create_engine("postgresql://dbuser:labtest321@db:5432/labdb", echo=True)

# db setup

def db_setup():
    SQLModel.metadata.create_all(engine, checkfirst=True)

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
        if not role2_exists_check:
            usuario_role = roles(nombre_rol="usuario")
            session.add(usuario_role)
            session.commit()

    with Session(engine) as session:
        admin_role_statement = select(users).where(users.username == "admin")
        admin_role_statement_check = session.exec(admin_role_statement).first()
        if admin_role_statement_check:
            create_user("admin", "admin", "pwd123", 1)

# db operations

def create_user(username: str, nombre_completo: str, password_sin_hashear: str, rol: int):
    with Session(engine) as session:
        clave_privada = password_sin_hashear #Tengo que llamar una funcion que genere la llave privada de la password
        new_user = users(username=username, nombre_completo=nombre_completo, password_encriptada=clave_privada, roles_id=rol)
        session.add(new_user)
        session.commit()
        print(f"Usuario {new_user.username}#{new_user.id} fue creado con el rol {new_user.roles_id}")