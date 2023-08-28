from generator_for_themes import parsing_only_buzzwords, get_themes_for_generation

def test_simple():
    
    text = '''
Hello
1. "Betrayed Desires: A Woman's Struggle for Love and Loyalty"
2. "Desperate Choices: A Woman's Fight for Freedom"
3. "The Weight of Secrets: A Woman's Battle for Redemption"
4. "Fading Echoes: A Woman's Journey from Loss to Healing"
5. "Broken Dreams: A Woman's Quest for Second Chances"
6. "Shattered Innocence: A Woman's Fight Against Injustice"
7. "Unforgiving Shadows: A Woman's Escape from a Dark Past"
8. "Lost Connections: A Woman's Struggle with Loneliness and Isolation"
9. "Haunted Memories: A Woman's Battle with Unresolved Trauma"
10. "Whispers of Deception: A Woman's search for Truth and Deceit"
11. "Scarlet Tears: A Woman's Path to Overcome Heartbreak"
12. "Tangled Fates: A Woman's struggle to Reclaim her Destiny"
13. "Crimson Desperation: A Woman's Fight for Survival"
14. "Fragile Hopes: A Woman's Battle against Societal Expectations"
15. "Stolen Identity: A Woman's Journey to Reclaim her True Self"
16. "No Escape: A Woman's Fight for Freedom from a Toxic Relationship"
17. "Abyss of Regrets: A Woman's Battle with Guilt and Remorse"
18. "Fading Reflections: A Woman's Struggle with Aging and Self-worth"
19. "Whispers of Betrayal: A Woman's Journey through Betrayal and Forgiveness"
20. "Beneath the Surface: A Woman's Quest to Uncover the Truth"
21. "Darkened Paths: A Woman's Struggle with Moral Dilemmas"
22. "Fractured Desires: A Woman's Battle between Passion and Responsibility"
23. "Silver Linings in Shadows: A Woman's Journey to Find Happiness Amidst Turmoil"
24. "Downward Spiral: A Woman's Escape from Self-Destruction"
25. "Guardians of Hope: A Woman's Fight for a Better Future"
Hello bey
'''
    only_buzzwords = parsing_only_buzzwords(text)
    assert len(only_buzzwords) == 25
    assert only_buzzwords[12] == 'Crimson Desperation: A Woman\'s Fight for Survival'
    assert only_buzzwords[6] == 'Unforgiving Shadows: A Woman\'s Escape from a Dark Past'


def test_get_themes_for_generation():
    themes = get_themes_for_generation()
    assert len(themes) > 100
    assert themes[0] == "Epic Fantasy"