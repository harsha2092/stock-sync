CREATE TABLE nse_daily_trade (
    security_id VARCHAR ( 50 ),
    equity_group VARCHAR ( 50 ),
    open decimal,
    high decimal,
    low decimal,
    close decimal,
    last decimal,
    prev_close decimal,
    no_of_shares decimal,
    net_turnover decimal,
    trading_date DATE,
    no_trades bigint,
    isin_no VARCHAR(50),
);

-- security_id,equity_group,open,high,low,close,last,prev_close,no_of_shares,net_turnover,trading_date,no_trades,isin_no
