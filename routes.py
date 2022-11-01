from flask import render_template, request
from app import app, users_list


@app.route('/users')
def users():
    term = request.args.get('term') or ''
    filtered_users = filter(lambda x: term in x, users_list)
    return render_template(
        'users/index.html',
        users=filtered_users,
        search=term,
    )


if __name__ == '__main__':
    app.run(debug=True)
