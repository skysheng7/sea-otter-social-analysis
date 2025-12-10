#!/usr/bin/env python3
"""
Sea Otter Social Analysis - Example Script

This script demonstrates basic data analysis setup for studying sea otter
social behavior, focusing on grooming and play patterns.

Author: Sea Otter Research Team
Date: December 2025
"""

import pandas as pd
import numpy as np
import scipy.stats as stats

def load_sample_data():
    """
    Create sample sea otter behavioral data for demonstration.
    
    In a real analysis, you would load your actual dataset here.
    """
    # Sample data structure for sea otter social interactions
    np.random.seed(42)  # For reproducible results
    
    n_observations = 100
    data = {
        'otter_id': [f'otter_{i:03d}' for i in range(1, 21)] * 5,
        'partner_id': np.random.choice([f'otter_{i:03d}' for i in range(1, 21)], n_observations),
        'behavior_type': np.random.choice(['grooming', 'play', 'rest', 'foraging'], n_observations, p=[0.3, 0.25, 0.25, 0.2]),
        'duration_minutes': np.random.exponential(scale=5, size=n_observations),
        'location': np.random.choice(['kelp_forest', 'rocky_shore', 'open_water'], n_observations),
        'time_of_day': np.random.choice(['morning', 'afternoon', 'evening'], n_observations)
    }
    
    return pd.DataFrame(data)

def analyze_grooming_patterns(df):
    """
    Analyze grooming behavior patterns in sea otters.
    """
    print("=== Grooming Behavior Analysis ===")
    
    # Filter for grooming behaviors
    grooming_data = df[df['behavior_type'] == 'grooming']
    
    print(f"Total grooming observations: {len(grooming_data)}")
    print(f"Average grooming duration: {grooming_data['duration_minutes'].mean():.2f} minutes")
    print(f"Median grooming duration: {grooming_data['duration_minutes'].median():.2f} minutes")
    
    # Grooming by location
    grooming_by_location = grooming_data.groupby('location')['duration_minutes'].agg(['count', 'mean'])
    print("\nGrooming patterns by location:")
    print(grooming_by_location)
    
    return grooming_data

def analyze_play_patterns(df):
    """
    Analyze play behavior patterns in sea otters.
    """
    print("\n=== Play Behavior Analysis ===")
    
    # Filter for play behaviors
    play_data = df[df['behavior_type'] == 'play']
    
    print(f"Total play observations: {len(play_data)}")
    print(f"Average play duration: {play_data['duration_minutes'].mean():.2f} minutes")
    print(f"Median play duration: {play_data['duration_minutes'].median():.2f} minutes")
    
    # Play by time of day
    play_by_time = play_data.groupby('time_of_day')['duration_minutes'].agg(['count', 'mean'])
    print("\nPlay patterns by time of day:")
    print(play_by_time)
    
    return play_data

def social_network_analysis(df):
    """
    Basic social network analysis of otter interactions.
    """
    print("\n=== Social Network Analysis ===")
    
    # Count interactions between otters
    social_interactions = df[df['behavior_type'].isin(['grooming', 'play'])]
    interaction_counts = social_interactions.groupby(['otter_id', 'partner_id']).size().reset_index(name='interaction_count')
    
    print(f"Total social interactions: {len(social_interactions)}")
    print(f"Unique otter pairs: {len(interaction_counts)}")
    
    # Most social otters
    most_social = social_interactions['otter_id'].value_counts().head(5)
    print("\nMost socially active otters:")
    print(most_social)
    
    return interaction_counts

def statistical_tests(df):
    """
    Perform basic statistical tests on the behavioral data.
    """
    print("\n=== Statistical Analysis ===")
    
    # Compare grooming vs play durations
    grooming_durations = df[df['behavior_type'] == 'grooming']['duration_minutes']
    play_durations = df[df['behavior_type'] == 'play']['duration_minutes']
    
    if len(grooming_durations) > 0 and len(play_durations) > 0:
        # Mann-Whitney U test (non-parametric)
        statistic, p_value = stats.mannwhitneyu(grooming_durations, play_durations, alternative='two-sided')
        
        print(f"Mann-Whitney U test comparing grooming vs play durations:")
        print(f"Statistic: {statistic:.2f}")
        print(f"P-value: {p_value:.4f}")
        
        if p_value < 0.05:
            print("Significant difference found between grooming and play durations!")
        else:
            print("No significant difference found between grooming and play durations.")

def main():
    """
    Main analysis pipeline for sea otter social behavior.
    """
    print("Sea Otter Social Behavior Analysis")
    print("=" * 40)
    
    # Load data
    df = load_sample_data()
    print(f"Loaded {len(df)} behavioral observations")
    print(f"Unique otters: {df['otter_id'].nunique()}")
    
    # Perform analyses
    grooming_data = analyze_grooming_patterns(df)
    play_data = analyze_play_patterns(df)
    interaction_data = social_network_analysis(df)
    statistical_tests(df)
    
    print("\n" + "=" * 40)
    print("Analysis complete! 🦦")
    print("\nNext steps:")
    print("1. Replace sample data with your actual sea otter dataset")
    print("2. Expand analysis with visualization (matplotlib, seaborn)")
    print("3. Add network analysis tools (networkx)")
    print("4. Implement more sophisticated statistical models")

if __name__ == "__main__":
    main()