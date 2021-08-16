from user_recipes_app import app
from user_recipes_app.models.user import User
from user_recipes_app.models.recipe import Recipe
from flask import render_template, request, redirect, session, flash

# Display Routes


@app.route('/recipes/new')
def recipe_new():
    if 'user_id' not in session:
        return redirect('/')
    return render_template('recipe_new.html')


@app.route('/recipes/<int:recipe_id>/edit')
def edit_recipe(recipe_id):
    data = {
        'recipe_id': recipe_id
    }
    recipe = Recipe.view(data)
    return render_template('recipe_edit.html', recipe=recipe)


@app.route('/recipes/<int:recipe_id>/view')
def recipe_view(recipe_id):
    if 'user_id' not in session:
        return redirect('/')
    data = {
        'recipe_id': recipe_id
    }
    get_user = {
        'id': session['user_id']
    }
    user = User.get_by_id(get_user)
    recipe = Recipe.view(data)
    return render_template('recipe_view.html', recipe=recipe, user=user)


# Action Routes


@app.route('/recipes/create', methods=["POST"])
def recipe_create():
    if 'user_id' not in session:
        return redirect('/')
    else:
        if not Recipe.validate_recipe(request.form):
            print('not true')
            return redirect('/recipes/new')
        else:
            data = {
                'name': request.form['name'],
                'desc': request.form['desc'],
                'under_30': request.form['under_30'],
                'instructions': request.form['instructions'],
                'created_at': request.form['dt']
            }
            new_recipe = Recipe.save(data)
            add_join = {
                'user_id': session['user_id'],
                'recipe_id': new_recipe
            }
            created_by = Recipe.add_recipe_to_user(add_join)
            print(created_by)
            return redirect('/users/dashboard')


@app.route('/recipes/update', methods=['POST'])
def recipe_update():
    if 'user_id' not in session:
        return redirect('/')
    data = {
        'id': request.form['recipe_id'],
        'name': request.form['name'],
        'desc': request.form['desc'],
        'instructions': request.form['instructions'],
        'under_30': request.form['under_30'],
        'date_updated': request.form['date_updated']
    }
    if not Recipe.validate_recipe(data):
        return redirect(f"/recipes/{request.form['recipe_id']}/edit")
    Recipe.update(data)
    return redirect('/users/dashboard')


@app.route('/recipes/<int:recipe_id>/delete')
def destroy(recipe_id):
    if 'user_id' not in session:
        return redirect('/')
    data = {
        'recipe_id':recipe_id
    }
    Recipe.delete(data)
    return redirect('/users/dashboard')