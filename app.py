import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
import datetime

#Configuraciones para firebase
cred = credentials.Certificate("todolistAccountKey.json")
fire = firebase_admin.initialize_app(cred)

#Conexion a firestore DB = DataBase
db = firestore.client()

#Se crea la referencia de la base de datos
tasks_ref = db.collection("tasks")
#Leer toda las tasks

def read_tasks():
    #docs = tasks_ref.stream()
    docs = tasks_ref.get()
    for task in docs:
        #print(task.to_dict())
        #print(type(task.to_dict()["fecha"]))
        print(f"ID: {task.id} => DATA:{task.to_dict()}")

# --- Leer una sola task ---
def read_task(id):
    task = tasks_ref.document("id").get( )
    print(task.to_dict())

# --- Crea la tarea ---
def create_task(task):
    new_task = {"name":task, 
            "check": False, 
            "fecha": datetime.datetime.now()}
    tasks_ref.document().set(new_task)        

# --- Actualizar la tarea ---
def update_task(id):
    tasks_ref.document(id).update({"check":True})

# --- Eliminar la tarea ---
def delete_task(id):
    delet = tasks_ref.document(id).delete()
    print(delet)    
# --- Completado de la tarea ---
def get_task_completed():
    completed = tasks_ref.where("check", "==", False).get()
    for task in completed:
        print(f"ID:{task.id} => DATA:{task.to_dict()}")


#create_task(new_task)
#name_task = input("\n Ingresa el nombre de la tarea: ")
#create_task(name_task)
#update_task("paiwIA05qT51TIS1NAXO")       
#delete_task("paiwIA05qT51TIS1NAXO")     

get_task_completed()