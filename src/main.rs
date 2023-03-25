use crate::profile::{create_profile, load_profile_list};
use clap::{Command, Arg};

mod filesystem;
mod profile; 

fn app() -> Command {
    Command::new("caesium_rich_presence")
        .about("A simple rich presence client for Discord")
        .version("2.0.0-dev")
        .arg_required_else_help(true)
        .subcommand_required(true)
        .subcommands([
                     Command::new("create")
                     .about("Create profile."),

                     Command::new("load")
                     .about("Load profile."),

                     Command::new("edit")
                     .about("Edit profile."),

                     Command::new("remove")
                     .about("Remove profile.")
        ])
}

fn main() {
    let args = app().get_matches();
    match args.subcommand() {
        Some(("create", _submatches)) => {
            create_profile().expect("TODO: panic message");
        },
        Some(("load", _submatches)) => load_profile_list(),

        Some(("edit", _submatches)) => println!("Test 3"),

        Some(("remove", _submatches)) => println!("Test 4"),

        _ => println!("Unknown command")
    }
}
