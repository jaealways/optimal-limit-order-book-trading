# optimal-limit-order-book-trading
Optimal Limit Order Book Trading Strategies with Stochastic Volatility in the Underlying Asset


## reference
[Optimal Limit Order Book Trading Strategies with Stochastic Volatility in the Underlying Asset](https://link.springer.com/article/10.1007/s10614-022-10272-4)

# Introduction

High-frequency trading (HFT) has made significant advancements and has a profound impact on market microstructure. To address the complex optimization challenges market makers encounter in determining optimal bid and ask prices, stochastic control theory is required. 
<br><br>

The review within the paper tracks the development of optimal market making strategies, incorporating elements like stochastic demand, optimal spreads, inventory constraints, market impact, and stochastic volatility. The paper puts forward a strategy for optimal quoting that accounts for stochastic volatility.
<br><br>


# A Market Making Optimization Problem in a Limit Order Book

Assume the midprice $S_t$ follows dynamics below in high-frequency trading, especially in Limit Order situation.

## Define terms

### Midprice and Volatility

We denote midprice $S_t$ and stochastic volatility $v_t$ as following differential equations.<br>

$dS_t = \mu dt + \sqrt{v_t} dB_t^1 + \varepsilon^+ dM_t^+ - \varepsilon^- dM_t^-$<br>
$dv_t = k(\theta - v_t)dt + \sigma \sqrt{v_t} dB_t^2$<br>
$dB_t^1 dB_t^2 = \rho dt,$

<br><br>
$B_t^1 \sim \text{Wiener Process}$<br>
$B_t^2 \sim \text{Wiener Process}$<br>
$M_t^{\pm} \sim \text{Poisson Process}$<br>

### Inventory of the market maker
We also consider inventory of market makers $q$ as following dynamics.<br>
$\Delta q_t = q_0 + N_t^{-} - N_t^{+}, \quad q_t \in \mathbb{Z}, \quad t \in [0, T],$
<br><br>
$N_t^{\pm} \sim \text{Counting Process}$<br>

### Wealth process
Based on inventory and stock price the cash of the traders changes. So we suppose the wealth process $X$ follows stochastic dynamics.<br>

$dX_t = p_t^{+} dN_t^{+} - p_t^{-} dN_t^{-}$ <br>
$= (S_t + \delta^{+}) dN_t^{+} - (S_t - \delta^{-}) dN_t^{-}.$

### The rate of execution
In limit order situations, we need to consider the rate of execution $\Lambda_t$. <br>

$\Lambda_t^{\pm}(\delta_t^{\pm}) = \lambda_t^{\pm} e^{-\kappa_t^{\pm}\delta_t^{\pm}}.$

## Maximize the expected cash value

Now, we can define the market maker's promblem to maximize the expected cash as a stochastic optimization problem.

### Value function
By considering the penalty of inventories, we can maximize the expected cash value at maturity time T as following equation.<br>

$W(t, x, S; q) = \sup_{(\delta_t^{+})_{t \leq s \leq T} \in \mathcal{A}} \left[ E\left(U(X_T, S_T; q_T)\right) - \varphi \int_t^T (q_s^\delta)^2 ds \right],$<br>

### Penalty function

In the value function, we can variate the constant to penalize in the value function with following midprice dynamics. <br>

$\text{Var} \left( \int_t^T q_s dS_s \right) = E\left[ \left( \int_t^T q_s dS_s \right)^2 \right] = E\left[ \int_t^T (q_s^\delta)^2 ds \right],$ <br>

As a result, Market maker wants to maximize profits, and also wants to remove the inventory penalization.<br>

[code implemenation of Market Making Optimization Problem](market_making_opt.py)


# Dynamic Programming Equation for the Value Function