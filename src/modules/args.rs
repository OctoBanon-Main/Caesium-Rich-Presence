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
        name: String
    },
    Remove
}