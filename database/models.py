from database.connection import conectar

def consultar_clientes(filtro_nome=""):
    conn = None
    try:
        conn = conectar()
        if conn is None:
            return []

        with conn.cursor() as cursor:
            query = "SELECT id_cliente, nome, endereco, telefone, email FROM clientes"
            if filtro_nome.strip():
                query += " WHERE nome LIKE %s"
                cursor.execute(query, (f"%{filtro_nome}%",))
            else:
                cursor.execute(query)

            clientes = cursor.fetchall()
        return clientes

    except Exception as e:
        print(f"Erro ao consultar clientes: {e}")
        return []
    
    finally:
        if conn:
            conn.close()

def inserir_cliente(nome, endereco, telefone, email):
    conn = None
    try:
        conn = conectar()
        if conn is None:
            return

        with conn.cursor() as cursor:
            cursor.execute("""
                INSERT INTO clientes (nome, endereco, telefone, email)
                VALUES (%s, %s, %s, %s)
            """, (nome, endereco, telefone, email))
            conn.commit()

    except Exception as e:
        print(f"Erro ao inserir cliente: {e}")
    finally:
        if conn:
            conn.close()
