CREATE TABLE users(

id SERIAL PRIMARY KEY,

telegram_id VARCHAR(50),

username VARCHAR(100),

balance DOUBLE PRECISION DEFAULT 0,

mining_balance DOUBLE PRECISION DEFAULT 0,

wallet TEXT,

mining_active BOOLEAN DEFAULT TRUE,

last_mine_time BIGINT

);