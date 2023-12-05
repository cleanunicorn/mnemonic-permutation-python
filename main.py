import itertools
from hdwallet import BIP44HDWallet
from hdwallet.cryptocurrencies import EthereumMainnet
from hdwallet.derivations import BIP44Derivation

MNEMONIC = "banana alien boat bone cat cloud dog dolphin hospital kiwi lion pizza"
DESIRED_ADDRESS = "0x67d37A4E1674e4CBf13d66B839010B31f63dd844"

iteration = 0

mnemonic_words = MNEMONIC.split(" ")

for permutation in itertools.permutations(mnemonic_words):
    current_mnemonic = " ".join(permutation)

    iteration += 1
    if (iteration % 1000) == 0:
        print("Iteration: ", iteration)

    bip44_hdwallet: BIP44HDWallet = BIP44HDWallet(cryptocurrency=EthereumMainnet)

    try:
        bip44_hdwallet.from_mnemonic(mnemonic=current_mnemonic)
    except:
        # print(f"Error: {e}")
        continue

    bip44_hdwallet.clean_derivation()

    bip44_derivation: BIP44Derivation = BIP44Derivation(
        cryptocurrency=EthereumMainnet, account=0, change=False, address=0
    )
    bip44_hdwallet.from_path(path=bip44_derivation)

    if bip44_hdwallet.address() == DESIRED_ADDRESS:
        print(
            f"(0) {bip44_hdwallet.path()} {bip44_hdwallet.address()} 0x{bip44_hdwallet.private_key()}"
        )
        print("Mnemonic: ", current_mnemonic)
