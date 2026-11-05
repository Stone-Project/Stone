// stone:job stone:math.saw_wave
// stone:function saw_wave_rs

#[no_mangle]
pub extern "C" fn saw_wave_rs(x: f64) -> f64 { x - x.floor() }
