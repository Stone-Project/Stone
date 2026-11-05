// stone:job stone:math.square_wave
// stone:function square_wave_rs

#[no_mangle]
pub extern "C" fn square_wave_rs(x: f64) -> f64 {
    if x.rem_euclid(2.0) < 1.0 { 1.0 } else { 0.0 }
}
