use clap::{Parser, Subcommand};

#[derive(Parser, Debug)]
pub struct Subcommands {
    #[command(subcommand)]
    pub command: Option<Commands>,
}

#[derive(Subcommand, Debug)]
pub enum Commands {
    Create {
        #[arg(short)]
        name: String,
        #[arg(short)]
        client_id: u64,
        #[arg(short)]
        details: String,
        #[arg(short)]
        state: String
    },
    Remove
}