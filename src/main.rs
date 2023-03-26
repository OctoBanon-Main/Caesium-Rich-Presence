use crate::profile::{create_profile};

use clap::{Arg, Command};

mod filesystem;
mod profile;

fn app() -> Command {
    Command::new(env!("CARGO_PKG_NAME"))
        .about(env!("CARGO_PKG_DESCRIPTION"))
        .version(env!("CARGO_PKG_VERSION"))
        .author(env!("CARGO_PKG_AUTHORS"))
        .arg_required_else_help(true)
        .subcommand_required(true)
        .subcommands([
                     Command::new("create")
                         .arg(
                        Arg::new("name")
                            .short('n')
                            .long("name")
                            .help("Sets name for new profile")
                            .num_args(1..)
                            .required(true)
                            .value_parser(clap::value_parser!(String))
                        )
                         .arg(
                             Arg::new("client-id")
                                 .short('c')

                         )
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
            create_profile().expect("Error: Can't create profile");
        },
        Some(("load", _submatches)) => println!("Test 2"),

        Some(("edit", _submatches)) => println!("Test 3"),

        Some(("remove", _submatches)) => println!("Test 4"),

        _ => println!("Unknown command")
    }
}
