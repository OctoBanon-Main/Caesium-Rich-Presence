mod modules;

use modules::args::{Commands, Subcommands};
use modules::profile_manager::{create_profile};
use clap::Parser;

fn main() {
    let arguments = Subcommands::parse();
    match &arguments.command {
        Some(Commands::Create {name}) => {
            create_profile(&name);
        }

        _ => {}
    }
}