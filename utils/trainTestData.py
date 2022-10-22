from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

def trainTestData(df):
    y = df['DEATH_EVENT']  # dependent variable
    x = df.drop("DEATH_EVENT", axis=1)  # independent variables

    # splliting training and testing data
    x_train, x_test, y_train, y_test = train_test_split(x, y,
                                                        test_size=0.2,
                                                        shuffle=True,
                                                        random_state=4)
    scaler = StandardScaler()  # to equally contribution of data we do standrization
    scaler.fit(x_train)
    x_train = scaler.transform(x_train)
    x_test = scaler.transform(x_test)

    return x_train, x_test, y_train, y_test