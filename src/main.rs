mod modules;

use modules::args::{Commands, Subcommands};
use clap::Parser;

fn main() {
    let arguments = Subcommands::parse();
    match &arguments.command {
        Some(Commands::Create { name }) => {
            println!("{:?}", name)
        }
        _ => {}
    }
}