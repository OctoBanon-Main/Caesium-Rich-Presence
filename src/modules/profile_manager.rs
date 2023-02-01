use clap::builder::Str;
use serde::{Serialize, Deserialize};
use serde_json::Result;
use std::fs;

#[derive(Serialize, Deserialize)]
struct Profile {
    client_id: u64,
    details: String,
    state: String,
}

pub fn create_profile(name: &String, client_id: &u64, details: &String, state: &String) -> Result<()> {
    let profile_struct = Profile {
        client_id: *client_id,
        details: details.to_string(),
        state: state.to_string(),
    };

    fs::create_dir_all("./profiles").expect("TODO: panic message");
    let path = "./profiles/";

    let json = serde_json::to_string_pretty(&profile_struct)?;
    fs::write(format!("{}{}{}", path, name, ".json"), json).expect("TODO: panic message");


    Ok(())
}