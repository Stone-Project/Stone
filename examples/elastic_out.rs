// stone:job stone:math.elastic_out
// stone:function elastic_out_rs

#[no_mangle]
pub extern "C" fn elastic_out_rs(t: f64) -> f64 {
    if t == 0.0 { 0.0 }
    else if t == 1.0 { 1.0 }
    else { 2.0_f64.powf(-10.0 * t) * (t * 10.0 - 0.75).sqrt() + 1.0 }
}
