
def main():
    first = "666c61677b68337834646563696d616c5f63346e5f62335f41424144424142457d"
    print(f"{bytes.fromhex(first).decode()}")

if __name__ == "__main__":
    main()
