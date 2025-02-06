import asyncio

async def periodic_task(interval_seconds):
    while True:
        print("Executing async task...")
        await asyncio.sleep(interval_seconds)

async def main():
    # Start the periodic task
    await asyncio.create_task(periodic_task(5))

    # Keep the main function running (or perform other tasks if needed)
    await asyncio.Event().wait()

# Run the event loop
if __name__ == "__main__":
    asyncio.run(main())