from django.urls import path
from test1.views import all_scores, new_score, edit_score, delete_score, table_results, show_table, main_view, under

urlpatterns = [
    path('all/', all_scores, name='all_scores'),
    path('index', main_view, name='index'),
    path('new', new_score, name='new_score'),
    path('edit/<int:id>', edit_score, name='edit_score'),
    path('delete/<int:id>', delete_score, name='delete_score'),
    path('table2/', table_results, name='table_results'),
    path('table/', show_table, name='show_table'),
    path('under/', under, name='under'),

]
