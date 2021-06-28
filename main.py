# #à installer à la maison : flask_cors, flask_rest
# from  flask import Flask, jsonify
#
#
# app = Flask(__name__)
#
# list_etudiants = [
#     {'id':1, 'nom':'Kapapa Jean-Costa', 'cotes':[5,6,4,7]},
#     {'id':2, 'nom':'Kalubi Lucienne', 'cotes':[8,6,9,7]},
#     {'id':3, 'nom':'Kabedi Félicité', 'cotes':[10,10,4,9]},
#     {'id':4, 'nom':'Kimina Gloire', 'cotes':[5,9,4,7]},
#     {'id':5, 'nom':'Mbombo Olive', 'cotes':[5,10,4,4]}
# ]
#
# @app.route('/etudiants')
# def get_all_etudiants():
#     reponse=jsonify(list_etudiants)
#     reponse.headers.add('Access-Control-Allow-Origin','*')
#     return reponse
#
# @app.route('/etudiants/<int:id>', methods=['GET'])
# def get_etudiant_by_id(id):
#     for etudiant in list_etudiants:
#         if etudiant['id']==id:
#             return jsonify(etudiant)
#         else:
#             return "Objet non exitant"
# if __name__ == '__main__':
#     app.run(debug=True)
#
#
