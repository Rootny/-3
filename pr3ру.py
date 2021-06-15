импортный  склеарн
из  склеарна . наборы данных  импорт  load_breast_cancer
из  склеарна . model_selection  импорт  train_test_split
из  склеарна . naive_bayes  импортировать  GaussianNB
из  склеарна . импорт показателей  precision_score
data  =  load_breast_cancer ()

label_names  =  данные [ 'target_names' ]
метки  =  данные [ 'цель' ]
feature_names  =  data [ 'feature_names' ]
особенности  =  данные [ 'данные' ]

print ( label_names , " \ n " )
печать ( метки [ 0 ], " \ n " )

# создадуние имен и значений функций
print ( имена_компонентов [ 0 ], " \ n " )
печать ( функции [ 0 ], " \ n " )

train , test , train_labels , test_labels  =  train_test_split ( функции , ярлыки , test_size  =  0.40 , random_state  =  42 )

gnb  =  GaussianNB ()
модель  =  гнб . подходят ( поезд , train_labels )

предс  =  гнб . предсказать ( проверить )
печать ( пред. , " \ п " )
печать ( accuracy_score ( test_labels , Preds ), " \ п " )

предс  =  гнб . предсказывать ( тренироваться )
печать ( пред. , " \ п " )
печать ( accuracy_score ( train_labels , Preds ), " \ п " )
