#encoding=utf8

import os
import FukuML.Utility as utility
import FukuML.RidgeRegression as ridge_regression

input_train_data_file = os.path.join(os.path.join(os.getcwd(), os.path.dirname(__file__)), 'dataset/valence_train.dataset')

cross_validator = utility.CrossValidator()

ridge_regression1 = ridge_regression.RidgeRegression()
ridge_regression1.load_train_data(input_train_data_file)
ridge_regression1.set_feature_transform('legendre', 2)
ridge_regression1.set_param(lambda_p=0)
ridge_regression2 = ridge_regression.RidgeRegression()
ridge_regression2.load_train_data(input_train_data_file)
ridge_regression2.set_feature_transform('legendre', 2)
ridge_regression2.set_param(lambda_p=0.01)

print("\n10 fold cross validation：")

cross_validator.add_model(ridge_regression1)
cross_validator.add_model(ridge_regression2)
avg_errors = cross_validator.excute()

print("\n各模型驗證平均錯誤：")
print(avg_errors)
print("\n最小平均錯誤值：")
print(cross_validator.get_min_avg_error())

print("\n取得最佳模型：")
best_model = cross_validator.get_best_model()
print(best_model)

best_model.init_W()
best_model.train()

future_data = '0.0611308372368 0.0993997525059 3.17633608873 0.132953956654 0.163512368184 0.503072895918 0.00506405087374 0.0893733831561 -22.5496609941 1.32324699673 -0.345225269858 0.34516680672 0.269770217731 0.309647315954 -0.0545042759923 0.0250885647672 -0.0285019114017 -0.10620350794 0.0737289154413 -0.00745469755966 0.143458919362 0.00996362049113 0.00494915381479 0.0181222784462 0.00284234355031 0.0121786765298 0.0439514676088 0.00263779777155 0.00929148554562 0.0175601069361 0.00507993062144 0.0515183703489 0.0157422828657 0.0234774404393 0.0151708007324 0.0245546553942 0.0729340394927 0.021180860721 0.0261936599263 0.157799684176 0.00258598213009 0.0285683560527 0.546304655876 0.354792276734 0.318920051295 0.306188848853 0.313373931365 0.293607625164 0.295339829901 0.291561861698 0.292302876248 0.273056898286 0.270365825981 0.263261093528 0.226518154186 0.00712250354361 0.00423522268612 0.0137749158595 0.0025418853949 0.00870657752457 0.0256002754709 0.00275885955851 0.0088471873835 0.0127131140983 0.00480639019267 0.0244055450361 0.0139045753192 0.00595031482948'
prediction = best_model.prediction(future_data, mode='future_data')
print(prediction)

input_test_data_file = os.path.join(os.path.join(os.getcwd(), os.path.dirname(__file__)), 'dataset/valence_test.dataset')
best_model.load_test_data(input_test_data_file)
print("W 平均錯誤值（Ein）：")
print(best_model.calculate_avg_error(best_model.train_X, best_model.train_Y, best_model.W))
print("W 平均錯誤值（Eout）：")
print(best_model.calculate_avg_error(best_model.test_X, best_model.test_Y, best_model.W))
