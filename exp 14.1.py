def survey_analytics_tool():
    # Pre-defined list of vote selections (simulating user responses or a dataset)
    vote_stream = [
        "Electronics", "Clothing", "Electronics", "Home & Kitchen", 
        "Clothing", "Electronics", "Books", "Clothing", "Clothing"
    ]
    
    # Dictionary to dynamically store and increment vote counters
    vote_tally = {}
    
    print("Processing vote selections from the list...")
    # Tally votes dynamically
    for category in vote_stream:
        if category in vote_tally:
            vote_tally[category] += 1
        else:
            vote_tally[category] = 1
            
    # Display the final tally results
    print("\n--- Final Vote Tally ---")
    for category, count in vote_tally.items():
        print(f"{category}: {count} vote(s)")
        
    # Determine the winner
    if not vote_tally:
        print("\nNo votes were cast.")
        return

    # Find the category with the maximum votes
    winner = max(vote_tally, key=vote_tally.get)
    max_votes = vote_tally[winner]
    
    print(f"\n🏆 The Winner is: {winner} with {max_votes} votes!")

# Run the survey tool
survey_analytics_tool()