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
                     .about("Create profile.")
        ])
}

fn main() {
    let args = app().get_matches();
    match args.subcommand() {
        Some(("create", _submatches)) => {
            let name = _submatches.get_one::<String>("name").expect("Error").to_string();
            create_profile(&name).expect("Error: Can't create profile");
        },

        _ => println!("Unknown command")
    }
}
