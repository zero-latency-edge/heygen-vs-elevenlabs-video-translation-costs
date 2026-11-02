#!/usr/bin/env python3
"""HeyGen vs ElevenLabs Video Translation & Dubbing TCO Calculator 2026."""
import argparse

def calculate(video_minutes=30):
    # HeyGen: Credit-based model. Creator ~$29/mo for 15 credits (~15 mins). Additional credits ~$2.00/min.
    heygen_base = 29.0
    heygen_included = 15
    heygen_overage = max(0, video_minutes - heygen_included) * 2.00
    heygen_total = heygen_base + heygen_overage

    # ElevenLabs: Pro Plan $82.50/mo (annual) includes 500k chars (~500 mins).
    eleven_total = 82.50

    savings = heygen_total - eleven_total

    print("=" * 65)
    print("HeyGen vs ElevenLabs: 30 Minutes Video Translation Cost")
    print("=" * 65)
    print(f"Monthly Video Volume:      {video_minutes} finished minutes")
    print(f"HeyGen Creator Total:      ${heygen_total:.2f}/mo ($2.00/extra credit)")
    print(f"ElevenLabs Pro Plan Total: ${eleven_total:.2f}/mo (Includes ~500 mins)")
    print(f"Monthly Cost Difference:   ${savings:.2f}/mo ({'ElevenLabs Cheaper' if savings > 0 else 'HeyGen Cheaper'})")
    print("=" * 65)
    return heygen_total, eleven_total, savings

if __name__ == "__main__":
    calculate()
