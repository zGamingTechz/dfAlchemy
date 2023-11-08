import pandas


def createDataframe(list, index= None, columns= None):
    if list.lower() == 'bhavya':
        raise Exception('You Found The Secret!')
    else:
        try:
            if columns is None:
                if index is None:
                    dataframe = pandas.DataFrame(
                        data=list
                    )
                    return dataframe
                else:
                    dataframe = pandas.DataFrame(
                        data=list,
                        index=index
                    )
                    return dataframe
            else:
                dataframe = pandas.DataFrame(
                    data=list,
                    columns=columns,
                    index=index
                )
                return dataframe
        except:
            errorMessage = 'Pass A List Dumbass'
            raise SyntaxError(errorMessage)
