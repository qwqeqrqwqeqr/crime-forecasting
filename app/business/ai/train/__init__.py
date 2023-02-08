

from lightgbm import LGBMClassifier
LGBM_MODEL = LGBMClassifier(learning_rate=0.1, max_depth=6, n_estimators=400, num_leaves=15, random_state=RANDOM_STATE)



