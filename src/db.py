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
    account_status: str  # A nivel de backend los valores posibles seran "activa", "desactivada"
    roles_id: int = Field(default=None, foreign_key="roles.id") # A nivel de backend los valores son 1 y 2, 1 para admin y 2 para user


engine = create_engine("postgresql://dbuser:labtest321@db:5432/labdb", echo=True)

# db setup

def db_setup():
    SQLModel.metadata.create_all(engine, checkfirst=True)

    with Session(engine) as session:
        role1_statement = select(roles).where(roles.id == 1)
        role1_exists_check = session.exec(role1_statement).first()
        if not role1_exists_check:
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
        if not admin_role_statement_check:
            create_user_db("admin", "admin", "pwd123", "activa", 1)

# db operations

def create_user_db(username: str, nombre_completo: str, password_sin_hashear: str, rol: int):
    with Session(engine) as session:
        # En produccion las contrasena se deben almacenar encriptadas, por el momento se almacenan en texto plano
        clave_privada = password_sin_hashear
        new_user = users(username=username, nombre_completo=nombre_completo, password_encriptada=clave_privada, account_status="activa", roles_id=rol)
        session.add(new_user)
        session.commit()

def delete_user_db(username:str):
    with Session(engine) as session:
        # Por motivos de seguridad lo mejor seria nunca borrar cuentas solo desactivarlas
        delete_select_statement = select(users).where(users.username == username)
        user = session.exec(delete_select_statement).first()
        if user and user.account_status != "desactivada":
            user.account_status = "desactivada"

def update_user_db(username:str, data: dict):
    with Session(engine) as session:
        statement = select(users).where(users.username == username)
        user = session.exec(statement).first()
        if user:
            if "password" in data:
                data["password_encriptada"] = data["password"]
                data.pop("password", None)

            for key,value in data.items():
                setattr(user, key, value)
                
            session.add(user)
            session.commit()
            session.refresh(user)