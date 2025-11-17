#!/bin/bash
# Simulate deprovisioning inactive users
inactive_users=("dave" "eve")

echo "Starting cleanup..."
for user in "${inactive_users[@]}"; do
  echo "Deprovisioning $user..."
done
echo "Cleanup complete!"
