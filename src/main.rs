use modules::{
    arguments::{Commands, Subcommands},
    profile::{create_profile, load_profile_list}
};
use clap::Parser;

fn main() {
    let arguments = Subcommands::parse();
    match &arguments.command {
        Some(Commands::Create) => {
            create_profile().expect("TODO: panic message");
        },
        Some(Commands::Load) => load_profile_list(),

        Some(Commands::Edit) => println!("Test 3"),

        Some(Commands::Remove) => println!("Test 4"),

        _ => println!("Unknown command")
    }
}
