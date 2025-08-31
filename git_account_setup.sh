#!/bin/bash

read -p "Enter your full name or username: " git_name
read -p "Enter your GitHub email address: " git_email
echo

# --- Step 2: Generate SSH Key ---
echo "--- Generating SSH Key ---"
SSH_DIR="$HOME/.ssh"
KEY_PATH="$SSH_DIR/github_key"

# Create .ssh directory if it doesn't exist
if [ ! -d "$SSH_DIR" ]; then
    echo "Creating .ssh directory at $SSH_DIR"
    mkdir -p "$SSH_DIR"
    chmod 700 "$SSH_DIR"
fi

# Check if the key already exists before generating
if [ -f "$KEY_PATH" ]; then
    echo "## SSH key already exists at $KEY_PATH. Skipping generation."
else
    echo "Generating a new ED25519 SSH key..."
    # ssh-keygen will automatically prompt you to enter a passphrase
    ssh-keygen -t ed25519 -f "$KEY_PATH" -C "$git_email"
    echo ">> SSH key generated successfully!"
fi
echo

# --- Step 3: Display Public Key and Pause ---
echo "--- Add Your Public Key to GitHub ---"
echo "Copy the entire block of text below (starting with 'ssh-ed25519')."
echo "Then, add it to your GitHub account here: https://github.com/settings/keys"
echo
cat "${KEY_PATH}.pub"
echo
read -p "Press [Enter] after you have added the key to GitHub to continue..."
echo

# --- Step 4: Configure Git ---
echo "--- Configuring Git Global Settings ---"
git config --global user.name "$git_name"
git config --global user.email "$git_email"
echo ">> Git global user.name and user.email have been set."
echo

# --- Step 5: Verify Configuration ---
echo "--- Verifying Setup ---"
echo "Your current global Git configuration is:"
git config --global --list
echo
echo "<><><> All done! Your device is ready to use with GitHub.<><><>"


