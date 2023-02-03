use serde::{Serialize, Deserialize};
use serde_json::Result;

use crate::filesystem::{create_profile_file, read_profile_directory};

#[derive(Serialize, Deserialize)]
struct Profile {
    client_id: u64,
    details: String,
    state: String,
    start_timestamp: bool,
    end_timestamp: u64,
    large_image_url: String,
    small_image_url: String,
    large_image_text: String,
    small_image_text: String,
}

pub fn create_profile() -> Result<()> {
    let data = r#"{"client_id": 1,"details": "Test","state": "Test","start_timestamp": true,"end_timestamp": 1337,"large_image_url": "Test","small_image_url": "Test","large_image_text": "Test","small_image_text": "Test","party_size": [1,5]}"#;

    let json = serde_json::to_string_pretty(&data)?;
    create_profile_file(&json);

    Ok(())
}

pub fn load_profile_list() {
    read_profile_directory();
}