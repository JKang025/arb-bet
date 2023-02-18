# Arb-Bet
This project finds arbitrage opportunities for League of Legends professional ESports matches. It takes and compares scores from four different betting websites: Pinnacle Sports, Luckbox, Vulkan Bet, and GGBet. Upon finding an opportunity, it notifies the user of the match and the calculated arb opportunity.

## Usage

## Overview
### Betting odds
There are many types of betting odds; the one that we use for arbitrage opportunity calculations is decimal odds. Let's say I bet on a team and it has odds of 2.5. If that team wins, I get a return of 2.5x the stake that I put in. If I bet $100 on the team, I get $250 returned. (This includes the stake, so I get a net profit of $150.) Other types of odds are common too, such as American odds or fractional odds, but we found that decimal odds were easiest to use.

The probability that a team will win is calculated by $1/\text{decimal odds}$. For example, $1/2.5 = 0.4 = 40%$ chance that this team will win. Notice that as the probability that the team wins decreases, the decimal odd increases.

The way betting sites generate profit is through manipulating betting odds such that they are stacked slightly in their favor regardless of which team wins or loses. Let's say that there's a 40% chance that a team wins. The reciprocal of this is the decimal odd, which is 2.5. Bettors decrease this number such that if I were to win, I would win less than the probability suggests I should. For example, if this is number is 2.4, my payout is treated as if my team had a 41.67% chance of winning instead of a 40% chance. Ideally, the sum of probabilites of each team winning should be 100%. Bettors decrease the decimal odds such that **the sum of winning probabilities is greater than 100.**

That's where arb betting comes in: we find matchups where the sum of winning probabilities is less than 100%. League of Legends is played by two teams, so this looks like: $$1/\text{decimal odds of Team A} + 1/\text{decimal odds of Team B} < 1$$.

We then bet on both sides, betting different amounts of money for each team such that we either make zero or positive profit regardless of who wins.
