from flask import render_template, redirect, session, request
from flask_app import app

from flask_app.models.users import User
from flask_app.models.recipes import Recipe


@app.route('/new/recipe')
def new_recipe():
    if 'user_id' not in session:
        return redirect('/')

    #Yo sé que en sesión tengo el id de mi usuario (session['user_id'])
    #Queremos una función que en base a ese id me regrese una instancia del usuario
    formulario = {"id": session['user_id']}

    user = User.get_by_id(formulario) #Recibo la instancia de usuario en base a su ID

    return render_template('new_recipe.html', user=user)

@app.route('/create/recipe', methods=['POST'])
def create_recipe():
    if 'user_id' not in session:
        return redirect('/')
    
    if not Recipe.valida_receta(request.form):
        return redirect('/new/recipe')
    
    Recipe.save(request.form)

    return redirect('/dashboard')

