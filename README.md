# optimal-limit-order-book-trading
Optimal Limit Order Book Trading Strategies with Stochastic Volatility in the Underlying Asset


## reference
[Optimal Limit Order Book Trading Strategies with Stochastic Volatility in the Underlying Asset](https://link.springer.com/article/10.1007/s10614-022-10272-4)

# Introduction

High-frequency trading (HFT) has made significant advancements and has a profound impact on market microstructure. To address the complex optimization challenges market makers encounter in determining optimal bid and ask prices, stochastic control theory is required. 
<br><br>

The review within the paper tracks the development of optimal market making strategies, incorporating elements like stochastic demand, optimal spreads, inventory constraints, market impact, and stochastic volatility. The paper puts forward a strategy for optimal quoting that accounts for stochastic volatility.


# A Market Making Optimization Problem in a Limit Order Book

Assume the midprice $S_t$ follows dynamics below in high-frequency trading.


$dS_t = \mu dt + \sqrt{v_t} dB_t^1 + \varepsilon^+ dM_t^+ - \varepsilon^- dM_t^-, \\
dv_t = k(\theta - v_t)dt + \sigma \sqrt{v_t} dB_t^2, \\
dB_t^1 dB_t^2 = \rho dt,$

We denote <br>
$B_t^1 \sim \text{Wiener}(t) \\
B_t^2 \sim \text{Wiener}(t) \\
M_t^{\pm} \sim \text{Poisson}(\lambda)$

[Check the code for Market Making Optimization Problem](market_making_opt.py)

