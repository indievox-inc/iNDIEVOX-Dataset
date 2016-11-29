#encoding=utf8

import os
import FukuML.Utility as utility
import FukuML.SupportVectorMachine as svm

input_train_data_file = os.path.join(os.path.join(os.getcwd(), os.path.dirname(__file__)), 'dataset/emotion_combine_song_train.dataset')

cross_validator = utility.CrossValidator()

svm_mc1 = svm.MultiClassifier()
svm_mc1.load_train_data(input_train_data_file)
svm_mc1.set_param(svm_kernel='soft_gaussian_kernel', C=1)
svm_mc2 = svm.MultiClassifier()
svm_mc2.load_train_data(input_train_data_file)
svm_mc2.set_param(svm_kernel='soft_gaussian_kernel', C=10)
svm_mc3 = svm.MultiClassifier()
svm_mc3.load_train_data(input_train_data_file)
svm_mc3.set_param(svm_kernel='soft_gaussian_kernel', C=100)

print("\n10 fold cross validation：")

cross_validator.add_model(svm_mc1)
cross_validator.add_model(svm_mc2)
cross_validator.add_model(svm_mc3)
avg_errors = cross_validator.excute()

print("\n各模型驗證平均錯誤：")
print(avg_errors)
print("\n最小平均錯誤率：")
print(cross_validator.get_min_avg_error())

print("\n取得最佳模型：")
best_model = cross_validator.get_best_model()
print(best_model)

best_model.init_W()
best_model.train()

future_data = '0.0278168491121 0.0153081289758 3.03709327891 0.10743602255 0.174952836962 0.134500894777 0.00925739148295 0.0366942618855 -26.8290719952 2.69594124651 -0.203409679263 0.342470125679 0.0519006783931 0.0648784790254 -0.026167369055 -0.0277357874536 -0.0510789186296 0.0561642315562 0.0752938427254 0.153650035253 0.127605292534 0.00863423677803 0.00152184278569 0.0204106055354 0.00385907385983 0.00643303725106 0.0664754818536 0.000427742323517 0.00384711991249 0.0210506305868 0.0026212179348 0.084477579473 0.00214533360639 0.0351469014209 0.014402078037 0.00807931335865 0.151337828964 0.0331761081113 0.035783858315 0.117572817372 0.00788392985423 0.0195270029154 1.0771998416 0.500765515478 0.407391990885 0.388138248445 0.349837805057 0.323575080213 0.316572581219 0.302399019865 0.301288751582 0.297389332643 0.293436670022 0.274136691773 0.243194311489 0.00840222842786 0.00195310984335 0.0163067807474 0.0036984957456 0.00659340861747 0.0345825711173 0.000583805340572 0.00441007481147 0.0160952923152 0.00300033987001 0.0420276434902 0.00241129512281 0.00762129685232'
prediction = best_model.prediction(future_data, mode='future_data')
print(prediction)

input_test_data_file = os.path.join(os.path.join(os.getcwd(), os.path.dirname(__file__)), 'dataset/emotion_combine_song_test.dataset')
best_model.load_test_data(input_test_data_file)
print("W 平均錯誤率（Ein）：")
print(best_model.calculate_avg_error_all_class(best_model.train_X, best_model.train_Y, best_model.W))
print("W 平均錯誤率（Eout）：")
print(best_model.calculate_avg_error_all_class(best_model.test_X, best_model.test_Y, best_model.W))
