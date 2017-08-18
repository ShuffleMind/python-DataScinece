def calc_data(typeAgg, stock):
    df_stock = pdr.get_data_yahoo(stock)
    
    if typeAgg == 'Média':
        df_stock = df_stock['Close'].mean()
        return df_stock
    elif typeAgg == 'Máximo':
        df_stock = df_stock['Close'].max()
        return df_stock
    elif typeAgg == 'Mínimo':
        df_stock = df_stock['Close'].min()
        return stock
