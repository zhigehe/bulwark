---
title: "How to modify or cancel a pending Ethereum transaction"
date: "2025-02-08 22:05:00"
summary: "Key takeawaysEthereum transactions require gas fees, which depend on the gas limit and gas price. Higher fees ensure faster processing by validators.Pending Ethereum transactions can be resolved. Speed up stuck transactions by increasing gas fees or cancel them with a replacement transaction using the same nonce.Some wallets allow in-app wallet..."
categories:
  - "Cointelegraph"
lang:
  - "en"
translations:
  - "en"
tags:
  - "Cointelegraph"
menu: ""
thumbnail: ""
lead: ""
comments: false
authorbox: false
pager: true
toc: false
mathjax: false
sidebar: "right"
widgets:
  - "search"
  - "recent"
  - "taglist"
---

**Key takeaways

* Ethereum transactions require gas fees, which depend on the gas limit and gas price. Higher fees ensure faster processing by validators.
* Pending Ethereum transactions can be resolved. Speed up stuck transactions by increasing gas fees or cancel them with a replacement transaction using the same nonce.
* Some wallets allow in-app wallet features to cancel stuck transactions.
* Monitoring network congestion and using tools like Etherscan Gas Tracker to set optimal gas fees allow for smoother transaction management.

Ethereum is a decentralized blockchain platform that enables developers to build and deploy smart contracts and decentralized applications (DApps).

Often referred to as the “world computer,” Ethereum goes beyond mere cryptocurrency transactions, enabling a secure, trustless, decentralized environment. The native cryptocurrency of the Ethereum network, Ether (ETH), is used to pay for transaction fees, making it an integral part of the ecosystem.

Navigating Ethereum transactions can sometimes be challenging, especially when a transaction gets stuck in a pending state. Understanding how to modify or cancel these transactions is crucial for efficient blockchain interactions.

This comprehensive article will walk you through the steps to address pending Ethereum transactions, ensuring you are well-equipped to handle such situations.**

**Understanding Ethereum transactions and gas fees**

Ethereum transactions are validated through a consensus mechanism called proof-of-stake (PoS), where network participants, known as validators, are responsible for confirming transactions and adding them to the blockchain. Validators are selected based on the amount of ETH they have staked, ensuring the security and integrity of the network.

Every time you hit “send” on Ethereum, you are entering a bidding war for the validator’s attention. Gas fees? That’s what you bid with.

This is because every Ethereum transaction requires a fee, known as gas, paid to validators for processing and validating transactions. The total fee is determined by two factors:

* **Gas limit:** The maximum amount of gas you are willing to spend on a transaction. Think of this as your tank size — this is the maximum gas you are willing to burn for the trip.
* **Gas price:** The amount you are willing to pay per unit of gas, typically measured in gwei (1 gwei = 0.000000001 ETH). The higher it is, the faster your ride.

Setting a low gas price can result in a delayed or stuck transaction, as validators prioritize transactions with higher fees. This issue becomes more pronounced during periods of network congestion.

***Did you know?** The highest gas fee ever paid on Ethereum was a staggering $24 million for a single transaction in 2021. The fee was reportedly an error made by a crypto exchange, highlighting the importance of double-checking transaction details before confirming a transaction. Thankfully, it was returned.*

**Why do transactions get stuck?**

Stuck transactions are the blockchain equivalent of waiting in a long queue — annoying but fixable. Transactions may remain pending due to:

* **Low gas fees:** If the gas price is set too low, validators might overlook your transaction in favor of those with higher fees.
* **Network congestion:** High network activity can lead to delays, especially for transactions with lower gas prices.
* **Nonce gaps:** Ethereum assigns a unique number, called a nonce, to each transaction from an address. If a transaction with a lower nonce is pending, subsequent transactions will also be delayed until the pending one is processed.

***Did you know?** The Ethereum blockchain processes transactions in order of their nonce values. If a low-nonce transaction is stuck, it can delay all subsequent transactions from the same wallet.*

Therefore, Ethereum transactions can go through different states depending on their status within the blockchain network. Here’s an overview of various transaction states and what they mean:

* **Pending:** A transaction is broadcasted to the network and is waiting to be validated. If it remains pending for too long, it often means the gas fee is too low to compete with other transactions in the current network conditions.
* **Queued:** This state occurs when a transaction is delayed because there is another pending transaction with a lower nonce in the same queue. Ethereum processes transactions in order of their nonce values, so any gap in the sequence will prevent queued transactions from being validated.
* **Cancelled:** A transaction in this state can no longer be validated. This happens when it is replaced by another transaction with the same nonce value but higher gas fees and nullified value or data fields. Cancelled transactions effectively remove the original request from being processed.
* **Replaced:** Similar to cancellation, this state indicates the transaction has been modified rather than nullified. A replacement is used to speed up processing or change specific values and data in the original request. To replace a transaction, you must resubmit it with the same nonce and a higher gas fee.
* **Failed:** A transaction ends in this state when it encounters an error. Common causes include insufficient gas to complete execution, errors in the smart contract logic or invalid instructions. Failed transactions are recorded on the blockchain but do not execute their intended function.

Understanding these states can help you troubleshoot and manage Ethereum transactions effectively, ensuring smoother interaction with the network.

**Steps to modify or cancel a pending Ethereum transaction**

When a transaction is stuck, you’ve got two main plays:

* **Speed up the transaction:** This involves resubmitting the same transaction with a higher gas fee to incentivize validators to process it faster.
* **Cancel the transaction:** This entails sending a new transaction with the same nonce but a higher gas fee, effectively overwriting the pending transaction.

It is important to note that once a transaction has been confirmed on the Ethereum blockchain, it is final and can no longer be sped up, reverted or canceled.

**Method 1: Speed up Ethereum transactions**

When Ethereum transactions are stuck in a pending state due to low gas fees or network congestion, you can take steps to speed them up. The key lies in increasing the gas fee, which incentivizes validators to prioritize your transaction. To speed up a pending or stuck transaction, you need to have enough ETH in your Ethereum account to cover the network fees.

Here’s how you could speed up ETH transactions:

**1. Use a wallet with transaction management features**

Wallets like MetaMask allow users to speed up stuck transactions directly. In MetaMask, you can find the “Speed up” option on your pending transaction. This feature lets you resubmit the same transaction with a higher gas fee, which increases the likelihood of validators processing it faster.

Steps in MetaMask:

![Speed up transaction feature in Metamask](https://s3.tradingview.com/news/image/cointelegraph:9107c8b8c094b-f33bc5c617e6664c06795c749b317235-resized.jpeg)

* Open MetaMask and navigate to the pending transaction in your “Activity” tab.
* Click on the “Speed up” button.
* Enter a higher gas fee (you can use tools like Etherscan Gas Tracker to determine an optimal fee).
* Confirm the new transaction to broadcast it to the network.

This process essentially replaces the original transaction with one that has the same nonce but higher gas fees, prompting faster execution.

**2. Manually replace the transaction**

If your wallet does not have a “Speed up” option, you can manually replace the transaction using the same nonce. This involves:

* Canceling the stuck transaction by submitting a new one with the same nonce and a higher gas fee.
* Sending ETH to your own wallet address with zero value or reexecuting the original transaction with updated gas settings.

**3. Choose the right gas fees**

To avoid stuck transactions, always select an appropriate gas fee when initiating a transaction. Many wallets, including MetaMask, offer suggested gas fees based on current network activity, but you can opt for higher fees for time-sensitive transactions.

Gas fee hacks: Not in a hurry? Wait for network traffic to cool down (non-peak hours) and save some ETH.

**Method 2: Cancel stuck Ethereum transactions**

You can cancel transactions that are pending for hours; however, once again, it is prudent to remember that once a transaction has been confirmed on the Ethereum blockchain, it is final and cannot be sped up, reverted or canceled.

Fortunately, there are two primary methods to cancel a pending Ethereum transaction: using the in-app feature of wallets like MetaMask or manually setting a custom nonce. Here’s how both methods work:

**1. Canceling a transaction in-app**

Many wallets, such as MetaMask, offer a built-in option to cancel pending transactions. This is the simplest and most user-friendly way to attempt a cancellation.

Steps:

* Open your MetaMask wallet and locate the pending transaction in the “Activity” section.

![Cancellation of Ethereum transaction in MetaMask application](https://s3.tradingview.com/news/image/cointelegraph:9107c8b8c094b-249ea98c0372cbd13e56f2ea9011a661-resized.jpeg)

* Select the “Cancel” option.
* Confirm the cancellation by signing a new transaction with a higher gas fee.

This method sends a replacement transaction with the same nonce as the pending one but without any value or data, effectively overriding the original transaction.

**2. Canceling a transaction using a custom nonce**

For advanced users or in cases where the wallet’s cancellation option is unavailable, you can manually cancel a transaction by using a custom nonce.

Steps:

* **Find the nonce of the stuck transaction:** Use a blockchain explorer to search for your wallet address. Locate the stuck transaction and note its nonce value.
* **Send a replacement transaction:**- Open your wallet and enable the “Custom Nonce” feature in the settings.- Create a new transaction to your own wallet address, setting the same nonce as the pending transaction.- Set the gas fee higher than the original transaction to ensure priority.

Once submitted, the new transaction will replace the pending one. This method works by using Ethereum’s rule that transactions must be processed in sequential order. By broadcasting a new transaction with the same nonce and higher gas fees, you effectively replace the pending one.

**Important considerations for canceling transactions**

* **No guarantees:** Attempting to cancel or speed up a transaction may not always be successful, especially during high network congestion.
* **Potential risks:** Incorrectly modifying transactions can lead to additional stuck transactions or unintended consequences. Ensure you understand the process thoroughly before proceeding.
* **Transaction finality:** Once a transaction is confirmed and included in a block, it cannot be reversed or modified. Always double-check transaction details before sending.

**Preventing future stuck transactions**

To minimize the risk of pending transactions:

* **Set appropriate gas fees:** Use tools like Etherscan’s Gas Tracker to determine optimal gas prices based on current network conditions.
* **Monitor network status:** Be aware of network congestion and adjust your transaction timing and fees accordingly.
* **Stay informed:** Regularly update your knowledge of Ethereum network operations and best practices to ensure smooth transactions.

By understanding the mechanics of Ethereum transactions and the tools available to you, you can effectively manage and resolve pending transactions, ensuring a seamless experience on the blockchain.

***Written by: Shailey Singh***

[Cointelegraph](https://www.tradingview.com/news/cointelegraph:9107c8b8c094b:0-how-to-modify-or-cancel-a-pending-ethereum-transaction/)
