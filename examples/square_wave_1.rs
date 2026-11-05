// stone:job stone:math.square_wave_1
// stone:function square_wave_1_rs

#[no_mangle]
pub extern "C" fn square_wave_1_rs(x: f64) -> f64 {
    if x.rem_euclid(1.0) < 0.5 { 1.0 } else { 0.0 }
}
