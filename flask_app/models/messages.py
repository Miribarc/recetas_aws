from flask_app.config.mysqlconnection import connectToMySQL

class Message:
    def __init__(self, data):
        self.id= data['id']
        self.content = data['content']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.sender_id = data['sender_id']
        self.receiver_id = data['receiver_id']
        self.sender_name = data['sender_name']
        self.receiver_name = data['receiver_name']

    @classmethod
    def save(cls, formulario):
        query = "INSERT INTO messages(content, sender_id, receiver_id) VALUES (%(content)s, %(sender_id)s, %(receiver_id)s)"
        result = connectToMySQL('muro_privado').query_db(query, formulario)
        return result

    @classmethod
    def get_user_messages(cls, formulario):
        query = "SELECT messages.*, receivers.first_name as receiver_name, senders.first_name as sender_name FROM messages LEFT JOIN users as receivers ON receivers.id = messages.receiver_id LEFT JOIN users as senders ON senders.id = messages.sender_id WHERE receiver_id = %(id)s;"
        results = connectToMySQL('muro_privado').query_db(query, formulario)
        messages = []
        for message in results:
            messages.append(cls(message)) #1.- cls(message) me crea una instancia de mensaje 2.- messages.append agreamos la instancia a la lista messages
        return messages

    @classmethod
    def eliminate(cls, formulario):
        #formulario = {id: 1} #Diccionario con id de mensaje que voy a eliminar
        query = "DELETE FROM messages WHERE id = %(id)s"
        result = connectToMySQL('muro_privado').query_db(query, formulario)
        return result


